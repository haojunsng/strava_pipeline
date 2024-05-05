from airflow.providers.amazon.aws.operators.ecs import EcsRunTaskOperator
from .settings import (
    GOMU_TASK_DEFINITION,
    ECS_CLUSTER,
    GOMU_CONTAINER_NAME,
    NETWORK_CONFIGURATION,
)


class StravaToS3Operator(EcsRunTaskOperator):
    """
    Custom StravaToS3Operator that inherits from EcsRunTaskOperator
    """

    def __init__(self, strava_id, **kwargs):
        super().__init__(
            task_definition=GOMU_TASK_DEFINITION,
            cluster=ECS_CLUSTER,
            overrides={
                "containerOverrides": [
                    {
                        "name": GOMU_CONTAINER_NAME,
                        "command": [f"python main.py {strava_id}"],
                    },
                ],
            },
            network_configuration=NETWORK_CONFIGURATION,
            **kwargs,
        )

    def execute(self, context):
        super().execute(context)