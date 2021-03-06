# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.parameters import tags_type, get_location_type, get_enum_type
from azext_rdbms_up.vendored_sdks.azure_mgmt_rdbms.mysql.models.my_sql_management_client_enums import (
    SslEnforcementEnum, GeoRedundantBackup
)


def load_arguments(self, _):  # pylint: disable=too-many-locals, too-many-statements
    with self.argument_context('mysql up') as c:
        c.argument('sku_name', options_list=['--sku-name'], default='GP_Gen5_4',
                   help='The name of the sku, typically, tier + family + cores, e.g. B_Gen4_1, GP_Gen5_8.')
        c.argument('backup_retention', type=int,
                   help='The number of days a backup is retained.')
        c.argument('geo_redundant_backup', arg_type=get_enum_type(GeoRedundantBackup),
                   default=GeoRedundantBackup.disabled.value, help='Enable Geo-redundant or not for server backup.')
        c.argument('storage_mb', options_list=['--storage-size'], type=int,
                   help='The max storage size of the server. Unit is megabytes.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('version', help='Server version', default='5.7')
        c.argument('server_name', options_list=['--server-name', '-s'], help='Name of the server.')
        c.argument('administrator_login', options_list=['--admin-user', '-u'], arg_group='Authentication',
                   help='The login username of the administrator.')
        c.argument('administrator_login_password', options_list=['--admin-password', '-p'], arg_group='Authentication',
                   help='The login password of the administrator.')
        c.extra('generate_password', help='Generate a password.', arg_group='Authentication')
        c.argument('ssl_enforcement', arg_type=get_enum_type(SslEnforcementEnum),
                   default=SslEnforcementEnum.disabled.value,
                   help='Enable ssl enforcement or not when connect to server.')
        c.argument('database_name', options_list=['--database-name', '-d'],
                   help='The name of a database to initialize.')
        c.argument('tags', tags_type)
