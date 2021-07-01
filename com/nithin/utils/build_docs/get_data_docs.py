import datetime
import great_expectations as ge
import great_expectations.jupyter_ux
from great_expectations.checkpoint import LegacyCheckpoint
from great_expectations.data_context.types.resource_identifiers import ValidationResultIdentifier
from pyhocon import ConfigFactory


def create_data_docs_util(context,conf):
    results = LegacyCheckpoint(
    name="_temp_checkpoint",
    data_context=context,
    batches=[
        {
          "batch_kwargs": conf.batch_kwargs,
          "expectation_suite_names": [conf.expectation_suite_name]
        }
    ]
).run()

    validation_result_identifier = results.list_validation_result_identifiers()[0]
    context.build_data_docs()
    context.open_data_docs(validation_result_identifier)