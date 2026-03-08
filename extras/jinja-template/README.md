# quickstart

- create the venv and activate it
    ```shell
    uv venv --python 3.14
    source .venv/bin/activate
    ```
- install the dependencies
    ```shell
    uv pip install -r requirements.txt
    ```
- generate the `YAML` file from the template
    ```shell
    python generate_yaml.py 
    ```

Example of the output:

```shell
$ head -n 30  yaml/output_sample.yaml 
#events
---

ID: cce26cf8-76fd-4beb-95c4-cba0506829e7
  name: amet diam in
  labels:
    - live
  location:
    address: 8237 Killdeer Circle
    town: Taplow
    postcode: SL3
  comment: nulla sed vel enim sit amet nunc viverra dapibus nulla suscipit ligula in lacus curabitur at ipsum
  date: 16-07-2025
  time: 14:59

ID: 72baf253-d7b2-4989-9ea9-5968a1cf8c9c
  name: vestibulum vestibulum
  labels:
    - food
  location:
    address: 40653 Messerschmidt Lane
    town: Ascot
    postcode: SL4
  comment: in hac habitasse platea dictumst etiam faucibus cursus urna ut tellus nulla ut erat id
  date: 28-04-2025
  time: 23:02

ID: 31ce1c31-897c-47c6-82e8-1d8be4d37646
  name: interdum eu tincidunt
  labels:
```

# notes

- [mockaroo](https://www.mockaroo.com/) for the mock data
