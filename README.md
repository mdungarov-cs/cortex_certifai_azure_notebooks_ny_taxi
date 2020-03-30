# Example Notebooks

This directory contains example Jupyter notebooks illustrating use of Certifai
in that environment

## Installation


### Pre-requisites

Create a suitable base python environment in which to work.  It is recommended
to use a virtual environment such as conda.  The environment should use
Python 3.6 (note - 3.7 is not currently supported for direct integration of the
Certifai engine package).

For example, with conda:
`conda create -n <Environment-name> python=3.6`

Switch into the environment you created.  For example with conda:
`conda activate <Environment-name>`

### From the unpacked distribution ZIP archive

If you are using the distributed ZIP archive containing these notebooks then
proceed as below having expanded the ZIP to a local directory:

1. Create a suitable virtual environment as above
2. `cd` into this directory
3. `pip install -r requirements.txt`
4. Install the Certifai common and engine packages:
   * `pip install packages/*`

### From a clone of the repository

If you are using a clone of the repository directly proceed as follows:

1. Create a suitable virtual environment as above
2. From the root of the repository run `make build_dev`
3. `cd` into the 'certifai_examples'
4. `pip install -r requirements.txt`
5. Install the Certifai common and engine packages:
   * `pip install ../certifai_common/build/dist/*`
   * `pip install ../certifai_engine/build/dist/*`
   * `pip install ../certifai_scanner/build/dist/*`

## Usage

In the directory containing the notebooks (examples/notebooks) start the Jupyter server: `jupyter notebook` and open an example
notebook, or create a new one.

