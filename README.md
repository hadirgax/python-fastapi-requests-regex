
# Python FastAPI that consumes a JSON payload

## Environment requirements

* [Make](https://www.gnu.org/software/make/)
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Environment Setup

* Create the conda environment
    ```bash
    $ make env-create
    ```
* Delete the conda environment
    ```bash
    $ make env-remove
    ```
* Update the conda environment
    ```bash
    $ make env-update
    ```

## App initialization
* Activate the conda environment using the command:
    ```bash
    $ conda activate pythonenv
    ```
* Start the application using the command:
    ```bash
    (pythonenv)$ make run-app
    ```

## Application Tests

### Testing the API
* Quick `Smoke Test` to ensure the setup of the API is working properly:
    ```bash
    (pythonenv)$ make smoke-test
    ```

### Unit tests
* N/A


### Performance Test
* N/A

### Authorization Header
* N/A
