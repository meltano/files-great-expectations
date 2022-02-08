# Great Expectations

[Great Expectations](https://docs.greatexpectations.io/docs/) helps data teams eliminate pipeline debt, through data testing, documentation, and profiling. From the documentation:

> Great Expectations is the leading tool for validating, documenting, and profiling your data to maintain quality and improve communication between teams. Head over to our [getting started](https://docs.greatexpectations.io/docs/tutorials/getting_started/intro) tutorial.

## Adding and Installing

Install with Meltano:

```bash
meltano add utility great_expectations
# now try it out!
meltano invoke great_expectations --help
```

If you are using Great Expectations to validate data in a database or warehouse, you
might need to install the appropriate drivers. Common options are supported by Great Expectations
as pip extras, and any additional packages you may want can be added too by configuring
a custom `pip_url` for the `great_expectations` utility:

```bash
# set the _pip_url extra setting
meltano config great_expectations set _pip_url "great_expectations[redshift]; awscli"
# re-install the great_expectations plugin for changes to take effect
meltano install utility great_expectations
```

## Getting Started

Great Expectations can be used in many ways, the following is how we chose to use GE in our own [Squared Project](https://gitlab.com/meltano/squared/-/tree/master).

### Our Approach

We primarily use `great_expectations` to test the boundaries of our dbt project; incoming raw data (defined as dbt sources) and our final dbt models that are consumed by downstream BI tools.
Both sets of expectations need to pass for a successful pipeline run.

To implement the above, we create 'expectation suites' for every table that we want to test, then 'checkpoints' for configuring a set of expectations that we want to run together.
Usually we will have a DAG which runs EL, a checkpoint for the raw data, all dbt models and lastly a checkpoint for final dbt output consumption models.

For example:

```bash
# Run the dbt_hub_metrics checkpoint to validate for failures
meltano --environment=prod invoke great_expectations checkpoint run dbt_hub_metrics

# Add a new expecation suite
meltano --environment=prod invoke great_expectations suite new

# Edit an existing suite
meltano --environment=prod invoke great_expectations suite edit dbt_hub_metrics

# Add a new checkpoint (one or more expectation suites to validate against)
meltano --environment=prod invoke great_expectations checkpoint add my_new_checkpoint
```

### Other Details

In our `great_expectations.yml` file and `checkpoints/*.yml` we templated out our secrets (i.e. AWS keys) and environment specific configurations (i.e. schema) so that we could pass those from our `.env` and `*meltano.yml` configurations.