# Generated by Django 3.0.3 on 2020-02-17 23:59

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web_api", "0008_payload_installation_id_idx"),
    ]

    operations = [
        migrations.CreateModel(
            name="PullRequestActivityProgress",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "min_date",
                    models.DateField(
                        help_text="Date we should use as our minimum date for future aggregation jobs. Anything before this date is 'locked'."
                    ),
                ),
            ],
            options={"db_table": "pull_request_activity_progress",},
        ),
    ]