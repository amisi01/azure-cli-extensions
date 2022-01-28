# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class AnalyticalStorageSchemaType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the types of schema for analytical storage.
    """

    WELL_DEFINED = "WellDefined"
    FULL_FIDELITY = "FullFidelity"

class ApiType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to indicate the API type of the restorable database account.
    """

    MONGO_DB = "MongoDB"
    GREMLIN = "Gremlin"
    CASSANDRA = "Cassandra"
    TABLE = "Table"
    SQL = "Sql"
    GREMLIN_V2 = "GremlinV2"

class AuthenticationMethod(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Which authentication method Cassandra should use to authenticate clients. 'None' turns off
    authentication, so should not be used except in emergencies. 'Cassandra' is the default
    password based authentication. The default is 'Cassandra'. 'Ldap' is in preview.
    """

    NONE = "None"
    CASSANDRA = "Cassandra"
    LDAP = "Ldap"

class BackupPolicyMigrationStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the status of migration between backup policy types.
    """

    INVALID = "Invalid"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"

class BackupPolicyType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the mode of backups.
    """

    PERIODIC = "Periodic"
    CONTINUOUS = "Continuous"

class BackupStorageRedundancy(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to indicate type of backup storage redundancy.
    """

    GEO = "Geo"
    LOCAL = "Local"
    ZONE = "Zone"

class CompositePathSortOrder(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Sort order for composite paths.
    """

    ASCENDING = "ascending"
    DESCENDING = "descending"

class ConflictResolutionMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the conflict resolution mode.
    """

    LAST_WRITER_WINS = "LastWriterWins"
    CUSTOM = "Custom"

class ConnectionState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of connection error that occurred.
    """

    UNKNOWN = "Unknown"
    OK = "OK"
    OPERATOR_TO_DATA_CENTER_NETWORK_ERROR = "OperatorToDataCenterNetworkError"
    DATACENTER_TO_DATACENTER_NETWORK_ERROR = "DatacenterToDatacenterNetworkError"
    INTERNAL_OPERATOR_TO_DATA_CENTER_CERTIFICATE_ERROR = "InternalOperatorToDataCenterCertificateError"
    INTERNAL_ERROR = "InternalError"

class ConnectorOffer(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The cassandra connector offer type for the Cosmos DB C* database account.
    """

    SMALL = "Small"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class CreateMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to indicate the mode of account creation.
    """

    DEFAULT = "Default"
    RESTORE = "Restore"

class DatabaseAccountKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the type of database account. This can only be set at database account creation.
    """

    GLOBAL_DOCUMENT_DB = "GlobalDocumentDB"
    MONGO_DB = "MongoDB"
    PARSE = "Parse"

class DataTransferComponent(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    COSMOS_DB_CASSANDRA = "CosmosDBCassandra"
    AZURE_STORAGE = "AzureStorage"

class DataType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The datatype for which the indexing behavior is applied to.
    """

    STRING = "String"
    NUMBER = "Number"
    POINT = "Point"
    POLYGON = "Polygon"
    LINE_STRING = "LineString"
    MULTI_POLYGON = "MultiPolygon"

class DefaultConsistencyLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The default consistency level and configuration settings of the Cosmos DB account.
    """

    EVENTUAL = "Eventual"
    SESSION = "Session"
    BOUNDED_STALENESS = "BoundedStaleness"
    STRONG = "Strong"
    CONSISTENT_PREFIX = "ConsistentPrefix"

class EnableFullTextQuery(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describe the level of detail with which queries are to be logged.
    """

    NONE = "None"
    TRUE = "True"
    FALSE = "False"

class IndexingMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the indexing mode.
    """

    CONSISTENT = "consistent"
    LAZY = "lazy"
    NONE = "none"

class IndexKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the type of index.
    """

    HASH = "Hash"
    RANGE = "Range"
    SPATIAL = "Spatial"

class KeyKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The access key to regenerate.
    """

    PRIMARY = "primary"
    SECONDARY = "secondary"
    PRIMARY_READONLY = "primaryReadonly"
    SECONDARY_READONLY = "secondaryReadonly"

class ManagedCassandraProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the resource at the time the operation was called.
    """

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"

class ManagedCassandraResourceIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the resource.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"

class MongoRoleDefinitionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether the Role Definition was built-in or user created.
    """

    BUILT_IN_ROLE = "BuiltInRole"
    CUSTOM_ROLE = "CustomRole"

class NetworkAclBypass(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates what services are allowed to bypass firewall checks.
    """

    NONE = "None"
    AZURE_SERVICES = "AzureServices"

class NodeState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The state of the node in Cassandra ring.
    """

    NORMAL = "Normal"
    LEAVING = "Leaving"
    JOINING = "Joining"
    MOVING = "Moving"
    STOPPED = "Stopped"

class NodeStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether the node is functioning or not.
    """

    UP = "Up"
    DOWN = "Down"

class NotebookWorkspaceName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DEFAULT = "default"

class OperationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Enum to indicate the operation type of the event.
    """

    CREATE = "Create"
    REPLACE = "Replace"
    DELETE = "Delete"
    SYSTEM_OPERATION = "SystemOperation"

class PartitionKind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the kind of algorithm used for partitioning. For MultiHash, multiple partition keys
    (upto three maximum) are supported for container create
    """

    HASH = "Hash"
    RANGE = "Range"
    MULTI_HASH = "MultiHash"

class PrimaryAggregationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The primary aggregation type of the metric.
    """

    NONE = "None"
    AVERAGE = "Average"
    TOTAL = "Total"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    LAST = "Last"

class PublicNetworkAccess(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Whether requests from Public Network are allowed
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ResourceIdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes
    both an implicitly created identity and a set of user assigned identities. The type 'None' will
    remove any identities from the service.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
    NONE = "None"

class RestoreMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the mode of the restore.
    """

    POINT_IN_TIME = "PointInTime"

class RoleDefinitionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether the Role Definition was built-in or user created.
    """

    BUILT_IN_ROLE = "BuiltInRole"
    CUSTOM_ROLE = "CustomRole"

class ServerVersion(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the ServerVersion of an a MongoDB account.
    """

    THREE2 = "3.2"
    THREE6 = "3.6"
    FOUR0 = "4.0"

class ServiceSize(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Instance type for the service.
    """

    COSMOS_D4_S = "Cosmos.D4s"
    COSMOS_D8_S = "Cosmos.D8s"
    COSMOS_D16_S = "Cosmos.D16s"

class ServiceStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the status of a service.
    """

    CREATING = "Creating"
    RUNNING = "Running"
    UPDATING = "Updating"
    DELETING = "Deleting"
    ERROR = "Error"
    STOPPED = "Stopped"

class ServiceType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """ServiceType for the service.
    """

    SQL_DEDICATED_GATEWAY = "SqlDedicatedGateway"
    DATA_TRANSFER = "DataTransfer"
    GRAPH_API_COMPUTE = "GraphAPICompute"
    MATERIALIZED_VIEWS_BUILDER = "MaterializedViewsBuilder"

class SpatialType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the spatial type of index.
    """

    POINT = "Point"
    LINE_STRING = "LineString"
    POLYGON = "Polygon"
    MULTI_POLYGON = "MultiPolygon"

class TriggerOperation(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The operation the trigger is associated with
    """

    ALL = "All"
    CREATE = "Create"
    UPDATE = "Update"
    DELETE = "Delete"
    REPLACE = "Replace"

class TriggerType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the Trigger
    """

    PRE = "Pre"
    POST = "Post"

class UnitType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of the metric.
    """

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNT_PER_SECOND = "CountPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
    MILLISECONDS = "Milliseconds"
