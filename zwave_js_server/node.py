"""Z-Wave node."""
from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    node_id: int
    index: int
    installer_icon: int
    user_icon: int
    status: int
    ready: bool
    device_class: dict  # XXXXXX NEEDS CLASS
    is_listening: bool
    is_frequent_listening: bool
    is_routing: bool
    max_baud_rate: int
    is_secure: bool
    version: int
    is_beaming: bool
    manufacturer_id: int
    product_id: int
    product_type: int
    firmware_version: str
    zwave_plus_version: int
    node_type: int
    role_type: int
    name: str
    location: str
    device_config: dict  # XXXXXX NEEDS CLASS
    label: str
    neighbors: List[int]
    endpoint_count_is_dynamic: bool
    endpoints_have_identical_capabilities: bool
    individual_endpoint_count: int
    aggregated_endpoint_count: int
    interview_attempts: int

    def receive_event(self, event: dict):
        """Receive an event."""
        if event["event"] == "value added":
            return

        if event["event"] == "value updated":
            return

        if event["event"] == "value removed":
            return

        if event["event"] == "metadata updated":
            return

        if event["event"] == "value notification":
            return

        if event["event"] == "notification":
            return

        if event["event"] == "interview failed":
            return

        if event["event"] == "firmware update progress":
            return

        if event["event"] == "firmware update finished":
            return

        if event["event"] == "wake up":
            return

        if event["event"] == "sleep":
            return

        if event["event"] == "dead":
            return

        if event["event"] == "alive":
            return

        if event["event"] == "interview completed":
            return

        if event["event"] == "ready":
            return

        # TODO decide what to do with unknown event
        print(f"Unhandled node event for node {self.node_id}: {event}")

    @classmethod
    def from_state(cls, data):
        return cls(
            node_id=data.get("nodeId"),
            index=data.get("index"),
            installer_icon=data.get("installerIcon"),
            user_icon=data.get("userIcon"),
            status=data.get("status"),
            ready=data.get("ready"),
            device_class=data.get("deviceClass"),
            is_listening=data.get("isListening"),
            is_frequent_listening=data.get("isFrequentListening"),
            is_routing=data.get("isRouting"),
            max_baud_rate=data.get("maxBaudRate"),
            is_secure=data.get("isSecure"),
            version=data.get("version"),
            is_beaming=data.get("isBeaming"),
            manufacturer_id=data.get("manufacturerId"),
            product_id=data.get("productId"),
            product_type=data.get("productType"),
            firmware_version=data.get("firmwareVersion"),
            zwave_plus_version=data.get("zwavePlusVersion"),
            node_type=data.get("nodeType"),
            role_type=data.get("roleType"),
            name=data.get("name"),
            location=data.get("location"),
            device_config=data.get("deviceConfig"),
            label=data.get("label"),
            neighbors=data.get("neighbors"),
            endpoint_count_is_dynamic=data.get("endpointCountIsDynamic"),
            endpoints_have_identical_capabilities=data.get(
                "endpointsHaveIdenticalCapabilities"
            ),
            individual_endpoint_count=data.get("individualEndpointCount"),
            aggregated_endpoint_count=data.get("aggregatedEndpointCount"),
            interview_attempts=data.get("interviewAttempts"),
        )
