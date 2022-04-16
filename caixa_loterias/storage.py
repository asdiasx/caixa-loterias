import pathlib
import hashlib
import zlib
import datetime as dt


def calculate_crc32(data: bytes) -> int:
    """
    Calculate CRC32 checksum
    """
    return zlib.crc32(data) & 0xffffffff


def get_filename(dataset: str, date: dt.date) -> str:
    """
    Get filename for dataset
    """
    return f"{dataset}_{date.strftime('%Y%m%d')}.json"


def write_file_data(data: bytes, filepath: pathlib.Path):
    """
    Write data to file
    """
    # Check if parent directory exists
    if not filepath.parent.exists():
        filepath.parent.mkdir(parents=True)
    with open(filepath, "wb") as f:
        f.write(data)


def save_dataset(data, dataset, datadir):
    """
    Save dataset to file
    """
    today = dt.date.today()
    filename = get_filename(dataset, today)
    filepath = datadir / dataset / filename
    write_file_data(data, filepath)
