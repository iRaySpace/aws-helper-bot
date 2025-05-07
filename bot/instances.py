import boto3

ec2 = boto3.resource('ec2')


def find_all_instances(query=None):
    if not query:
        return ec2.instances.all()
    return ec2.instances.filter(Filters=_get_filters(query))


def _get_filters(query):
    query_data = [x for x in query.split(',')]
    return [_get_filter(x) for x in query_data]


def _get_filter(kv_data):
    key, value = kv_data.split('=')
    return {'Name': key, 'Values': [value]}
