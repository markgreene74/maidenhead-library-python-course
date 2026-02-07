# Local development

Run the notebook locally, make changes to the requirements.

## set up the environment

- create a virtual environment
    ```shell
    uv venv --python 3.14 .venv
    ```
- activate the virtual environment
    ```shell
    source .venv/bin/activate
    ```
- install the dependencies
    ```
    uv pip install -r requirements.txt
    ```

## add or update dependencies

- install new dependencies, for example
    ```shell
    uv pip install pandas numpy matplotlib seaborn
    ```
- upgrade existing dependencies
    ```shell
    uv pip install -r requirements.txt --upgrade
    ```
- update the requirements file
    ```shell
    uv pip freeze > requirements.txt
    ```

## run JupyterLab

- make sure JupyterLab dependencies are installed
    ```shell
    uv pip install -r requirements-jupyter.txt
    ```
- start JupyterLab
    ```shell
    uv run jupyter-lab
    ```
- (optional) start JupyterLab (access remotely)
    ```shell
    uv run jupyter-lab --no-browser --ip 0.0.0.0
    ```

