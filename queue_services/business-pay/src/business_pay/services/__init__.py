
from .nats_queue import NatsQueue
from gcp_queue import GcpQueue

gcp_queue = GcpQueue()
nats_queue = NatsQueue()

def create_filing_msg(identifier):
    """Create the filing payload."""
    filing_msg = {'filing': {'id': identifier}}
    return filing_msg

def create_email_msg(identifier, filing_type):
    email_msg = {'email': {'filingId': identifier, 'type': filing_type}}
    return email_msg
