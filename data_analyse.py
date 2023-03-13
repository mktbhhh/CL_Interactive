import argparse
import json
from types import SimpleNamespace
from dataset import Data_WithContext, Data_WithoutContext

if __name__ == "__main__":
    # torch.cuda.set_device(1)
    parser = argparse.ArgumentParser()
    # You can also use the parser to adjust hyparameters
    parser.add_argument("--local_rank", default=0, help="used for distributed parallel")
    parser.add_argument(
        "--distributed", action="store_true", help="if distributed train."
    )
    parser.add_argument("--block_num", type=int, default=0, help="block num")
    parser.add_argument("--block_size", type=int, default=0, help="block size")
    parser.add_argument("--temp", type=float, default=0, help="block size")
    args = parser.parse_args()

    config_file = "config/hyparam.json"
    with open(config_file) as fin:
        config = json.load(fin, object_hook=lambda d: SimpleNamespace(**d))
    data = Data_WithContext(
        config=config, max_seq_len=config.max_seq_len, model_type=config.model_type
    )

    train_set, dev_set = data.load_train_and_dev_files(
        train_file=config.train_file_path,
        dev_file=config.dev_file_path,
        # hard_sample_con=False,
        noisy=False,
    )
