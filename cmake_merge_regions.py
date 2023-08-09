from tools.config import Config, Target, Region
from tools.regions import merge_region_list
import os
import argparse
import logging

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__name__)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target', type=str, help="target device")
    parser.add_argument('build_path', type=str, help="path to build dirctory")
    parser.add_argument('basename', type=str, help="binary basename")
    args = parser.parse_args()

    Target.add_extra_targets(PROJECT_ROOT)

    config = Config(tgt=args.target, app_config=os.path.join(PROJECT_ROOT,"mbed_app.json"))

    regions = list(config.regions)

    for index, region in enumerate(regions):
        if (region.name == "application"):
            regions[index] =  Region(region.name, region.start, region.size, region.active, os.path.join(args.build_path, f"{args.basename}_application.bin"))
        
    print(regions)
    notify = logging.getLogger(__name__)

    merge_region_list(regions, os.path.join(args.build_path, f"{args.basename}.bin"), notify)

