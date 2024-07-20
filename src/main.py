import sys
import os
import argparse

# Add the src directory to the Python path
sys.path.append(os.path.dirname(__file__))

from core.key_sequence_replacer import KeySequenceReplacer

if __name__ == "__main__":
    # Argument parser to get command line arguments for YAML file path, delay, and device path
    parser = argparse.ArgumentParser(description='Key sequence replacer')
    parser.add_argument('--yaml_path', type=str, required=True, help='Path to the YAML file with key sequences')
    parser.add_argument('--delay', type=float, required=True, help='Delay between key presses for emulating human typing')
    parser.add_argument('--device_path', type=str, required=True, help='Path to the input device')

    args = parser.parse_args()

    # Create an instance of KeySequenceReplacer and start the replacer
    replacer = KeySequenceReplacer(args.yaml_path, args.delay, args.device_path)
    replacer.start()
