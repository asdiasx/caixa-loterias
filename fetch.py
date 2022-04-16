import argparse
import pathlib

from caixa_loterias import fetcher, meta, storage


def get_parser():
    parser = argparse.ArgumentParser(description="Fetch data from Caixa Loterias")
    parser.add_argument(
        "--datadir",
        default="/data-raw/caixa-loterias",
        type=pathlib.Path,
    )
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    datadir = args.datadir
    for dataset in meta.DATASETS:
        url = meta.get_url(dataset)
        print(f"Fetching {dataset} from {url}")
        data = fetcher.fetch(url)
        storage.save_dataset(data, dataset, datadir)


if __name__ == "__main__":
    main()
