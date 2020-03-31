import i18n

from resource.resource_reader import ResourceReader

path = ResourceReader().get_resource_path('locale')

i18n.set('file_format', 'json')
i18n.load_path.append(path)

i18n.set("locale", "pt_BR")

_ = i18n.t
