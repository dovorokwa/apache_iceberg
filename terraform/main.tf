
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "raw" {
  bucket = "nyc-taxi-raw-data-bucket"
}

resource "aws_s3_bucket" "iceberg" {
  bucket = "nyc-taxi-iceberg-bucket"
}

resource "aws_iam_role" "glue_role" {
  name = "GlueServiceRole"
  assume_role_policy = data.aws_iam_policy_document.glue_assume_role.json
}

data "aws_iam_policy_document" "glue_assume_role" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type = "Service"
      identifiers = ["glue.amazonaws.com"]
    }
  }
}
