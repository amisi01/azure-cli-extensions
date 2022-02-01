# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-statements
from azure.cli.core.commands import CliCommandType
from azext_cosmosdb_preview._client_factory import (
    cf_cassandra_cluster,
    cf_cassandra_data_center,
    cf_graph_resources,
    cf_service,
    cf_mongo_db_resources,
    cf_gremlin_resources,
    cf_table_resources,
    cf_restorable_sql_containers,
    cf_restorable_mongodb_collections,
    cf_restorable_gremlin_databases,
    cf_restorable_gremlin_graphs,
    cf_restorable_gremlin_resources,
    cf_restorable_tables,
    cf_restorable_table_resources
)

from azure.cli.command_modules.cosmosdb._client_factory import cf_db_accounts

def load_command_table(self, _):
    cosmosdb_graph_resources_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#GraphResourcesOperations.{}',
        client_factory=cf_graph_resources)

    cosmosdb_service_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#ServiceOperations.{}',
        client_factory=cf_service)

    cosmosdb_managed_cassandra_cluster_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#CassandraClustersOperations.{}',
        client_factory=cf_cassandra_cluster)

    cosmosdb_managed_cassandra_datacenter_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#CassandraDataCentersOperations.{}',
        client_factory=cf_cassandra_data_center)

    cosmosdb_rbac_mongo_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#MongoDBResourcesOperations.{}',
        client_factory=cf_mongo_db_resources)

    with self.command_group('managed-cassandra cluster', cosmosdb_managed_cassandra_cluster_sdk, client_factory=cf_cassandra_cluster) as g:
        g.custom_command('create', 'cli_cosmosdb_managed_cassandra_cluster_create', supports_no_wait=True)
        g.custom_command('update', 'cli_cosmosdb_managed_cassandra_cluster_update', supports_no_wait=True)
        g.custom_command('backup list', 'cli_cosmosdb_managed_cassandra_cluster_list_backup', is_preview=True)
        g.custom_command('backup show', 'cli_cosmosdb_managed_cassandra_cluster_show_backup', is_preview=True)
        g.custom_command('list', 'cli_cosmosdb_managed_cassandra_cluster_list')
        g.show_command('show', 'get')
        g.command('delete', 'begin_delete', confirmation=True, supports_no_wait=True)

    with self.command_group('managed-cassandra datacenter', cosmosdb_managed_cassandra_datacenter_sdk, client_factory=cf_cassandra_data_center) as g:
        g.custom_command('create', 'cli_cosmosdb_managed_cassandra_datacenter_create', supports_no_wait=True)
        g.custom_command('update', 'cli_cosmosdb_managed_cassandra_datacenter_update', supports_no_wait=True)
        g.command('list', 'list')
        g.show_command('show', 'get')
        g.command('delete', 'begin_delete', confirmation=True, supports_no_wait=True)

    with self.command_group('cosmosdb graph', cosmosdb_graph_resources_sdk, client_factory=cf_graph_resources, is_preview=True) as g:
        g.custom_command('create', 'cli_cosmosdb_graph_create', supports_no_wait=True)
        g.custom_command('exists', 'cli_cosmosdb_graph_exists')
        g.command('list', 'list_graphs')
        g.show_command('show', 'get_graph')
        g.command('delete', 'begin_delete_graph_resource', confirmation=True, supports_no_wait=True)

    with self.command_group('cosmosdb service', cosmosdb_service_sdk, client_factory=cf_service, is_preview=True) as g:
        g.custom_command('create', 'cli_cosmosdb_service_create', supports_no_wait=True)
        g.custom_command('update', 'cli_cosmosdb_service_update', supports_no_wait=True)
        g.command('list', 'list')
        g.show_command('show', 'get')
        g.command('delete', 'begin_delete', confirmation=True, supports_no_wait=True)

    with self.command_group('cosmosdb mongodb role definition', cosmosdb_rbac_mongo_sdk, client_factory=cf_mongo_db_resources) as g:
        g.custom_command('create', 'cli_cosmosdb_mongo_role_definition_create')
        g.custom_command('update', 'cli_cosmosdb_mongo_role_definition_update')
        g.custom_command('exists', 'cli_cosmosdb_mongo_role_definition_exists')
        g.command('list', 'list_mongo_role_definitions')
        g.show_command('show', 'get_mongo_role_definition')
        g.command('delete', 'begin_delete_mongo_role_definition', confirmation=True)

    with self.command_group('cosmosdb mongodb user definition', cosmosdb_rbac_mongo_sdk, client_factory=cf_mongo_db_resources) as g:
        g.custom_command('create', 'cli_cosmosdb_mongo_user_definition_create')
        g.custom_command('update', 'cli_cosmosdb_mongo_user_definition_update')
        g.custom_command('exists', 'cli_cosmosdb_mongo_user_definition_exists')
        g.command('list', 'list_mongo_user_definitions')
        g.show_command('show', 'get_mongo_user_definition')
        g.command('delete', 'begin_delete_mongo_user_definition', confirmation=True)

    # restorable accounts api
    cosmosdb_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#DatabaseAccountsOperations.{}',
        client_factory=cf_db_accounts)

    # restorable sql/mongodb apis
    cosmosdb_restorable_sql_containers_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#RestorableSqlContainersOperations.{}',
        client_factory=cf_restorable_sql_containers)

    cosmosdb_restorable_mongodb_collections_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#RestorableMongodbCollectionsOperations.{}',
        client_factory=cf_restorable_mongodb_collections)

    # restorable gremlin apis
    cosmosdb_gremlin_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.cosmosdb.operations#GremlinResourcesOperations.{}',
        client_factory=cf_gremlin_resources)

    cosmosdb_restorable_gremlin_databases_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#RestorableGremlinDatabasesOperations.{}',
        client_factory=cf_restorable_gremlin_databases)

    cosmosdb_restorable_gremlin_graphs_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#RestorableGremlinGraphsOperations.{}',
        client_factory=cf_restorable_gremlin_graphs)

    cosmosdb_restorable_gremlin_resources_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#RestorableGremlinResourcesOperations.{}',
        client_factory=cf_restorable_gremlin_resources)

    # restorable table apis
    cosmosdb_table_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.cosmosdb.operations#TableResourcesOperations.{}',
        client_factory=cf_table_resources)

    cosmosdb_restorable_tables_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#RestorableTablesOperations.{}',
        client_factory=cf_restorable_tables)

    cosmosdb_restorable_table_resources_sdk = CliCommandType(
        operations_tmpl='azext_cosmosdb_preview.vendored_sdks.azure_mgmt_cosmosdb.operations#RestorableTableResourcesOperations.{}',
        client_factory=cf_restorable_table_resources)

    # define commands
    with self.command_group('cosmosdb', cosmosdb_sdk, client_factory=cf_db_accounts) as g:
        g.show_command('show', 'get')
        g.custom_command('restore', 'cli_cosmosdb_restore', is_preview=True)
        g.custom_command('create', 'cli_cosmosdb_create')
        g.custom_command('update', 'cli_cosmosdb_update')
        g.custom_command('list', 'cli_cosmosdb_list')

    with self.command_group('cosmosdb sql restorable-container', cosmosdb_restorable_sql_containers_sdk, client_factory=cf_restorable_sql_containers, is_preview=True) as g:
        g.command('list', 'list')

    with self.command_group('cosmosdb mongodb restorable-collection', cosmosdb_restorable_mongodb_collections_sdk, client_factory=cf_restorable_mongodb_collections, is_preview=True) as g:
        g.command('list', 'list')
    
    with self.command_group('cosmosdb gremlin restorable-database', cosmosdb_restorable_gremlin_databases_sdk, client_factory=cf_restorable_gremlin_databases, is_preview=True) as g:
        g.command('list', 'list')

    with self.command_group('cosmosdb gremlin restorable-graph', cosmosdb_restorable_gremlin_graphs_sdk, client_factory=cf_restorable_gremlin_graphs, is_preview=True) as g:
        g.command('list', 'list')

    with self.command_group('cosmosdb gremlin restorable-resource', cosmosdb_restorable_gremlin_resources_sdk, client_factory=cf_restorable_gremlin_resources, is_preview=True) as g:
        g.command('list', 'list')

    with self.command_group('cosmosdb table restorable-table', cosmosdb_restorable_tables_sdk, client_factory=cf_restorable_tables, is_preview=True) as g:
        g.command('list', 'list')

    with self.command_group('cosmosdb table restorable-resource', cosmosdb_restorable_table_resources_sdk, client_factory=cf_restorable_table_resources, is_preview=True) as g:
        g.command('list', 'list')

    # Retrieve backup info for gremlin
    with self.command_group('cosmosdb gremlin', cosmosdb_gremlin_sdk, client_factory=cf_gremlin_resources) as g:
        g.custom_command('retrieve-latest-backup-time', 'cli_gremlin_retrieve_latest_backup_time')

    # Retrieve backup info for table
    with self.command_group('cosmosdb table', cosmosdb_table_sdk, client_factory=cf_table_resources) as g:
        g.custom_command('retrieve-latest-backup-time', 'cli_table_retrieve_latest_backup_time')
