BaseDir = './test'

models_to_dump = [
    {
        "name": 'health.Disease',
        'excluded_fields': [
            'state',
            'cuserid',
            'cdate',
            'version',
        ],
        'many_to_many_fields':[
            'disease_group_list'
        ]
    }
]