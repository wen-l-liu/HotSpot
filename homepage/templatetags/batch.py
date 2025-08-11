from django import template

register = template.Library()

@register.filter
def batch(value, batch_size):
    """Break a list into batches of batch_size."""
    value = list(value)
    batch_size = int(batch_size)
    return [value[i:i + batch_size] for i in range(0, len(value), batch_size)]