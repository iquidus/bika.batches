from bika.lims.exportimport.dataimport import SetupDataSetList as SDL


class SetupDataSetList(SDL):

    def __call__(self):
        return SDL.__call__(self, projectname="bika.batches")
