import argparse
import logging
import os
import pathlib
import shutil

import numpy as np
import osgeo.gdal_array


def read_tifs_to_numpy(data_dir: pathlib.Path) -> np.ndarray:
    """Create a numpy array from all .tif files in a directory."""
    images = []
    
    for image_path in data_dir.glob('*.tif'):
        image = osgeo.gdal_array.LoadFile(str(image_path))
        images.append(image)

    return np.asarray(images)


def save_numpy(
    data_dir: pathlib.Path,
    filename: str,
    data: np.ndarray,
    exist_ok: bool = False,
) -> None:
    """Save numpy array to file."""
    if not exist_ok and data_dir.exists():
        shutil.rmtree(data_dir)

    data_dir.mkdir(parents=True, exist_ok=exist_ok)

    with open(data_dir / filename, 'wb') as f:
        np.save(f, data)


def convert_tifs_to_numpy(
    logger: logging.Logger,
    input_data_dir: pathlib.Path,
    output_data_dir_base: pathlib.Path,
    output_filename: str = 'data.npy',
) -> None:
    dir_basename = os.path.basename(input_data_dir)
    output_data_dir = output_data_dir_base / dir_basename

    logger.info(f'Reading images from {input_data_dir}')
    images = read_tifs_to_numpy(input_data_dir)

    logger.info(f'Saving images to {output_data_dir / output_filename}')
    save_numpy(output_data_dir, output_filename, images)

    logger.info(f'Finished processing files {input_data_dir}')


def main():
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("input_data_dir_base")
    parser.add_argument("output_data_dir_base")
    args = parser.parse_args()

    input_data_dir_base = pathlib.Path(args.input_data_dir_base)
    output_data_dir_base = pathlib.Path(args.output_data_dir_base)

    data_dirs = input_data_dir_base.glob('*/')
    logger.info(f'Processing images from {input_data_dir_base}')
    
    for data_dir in data_dirs:
        convert_tifs_to_numpy(
            logger,
            input_data_dir=data_dir,
            output_data_dir_base=output_data_dir_base,
        )

    logger.info(f'Finished processing all subdirectories of {input_data_dir_base}')
    logger.info(f'Converted files are in {output_data_dir_base}')


if __name__ == "__main__":
    main()
