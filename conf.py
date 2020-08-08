BaseDir = 'PATH_TO_SAVED_AND_READ_JSON'

models_to_dump = [
    {
        "name": 'APP.MODELNAME',
        'excluded_fields': [
            'state',
            'cuserid',
            'cdate',
            'version',
        ],
        'many_to_many_fields':[]
    }
]
