import pypyrus_etl as etl

class Extractor(etl.Extractor):
    def run(self):
        self.pipeline.input.select_files()
        self.pipeline.input.push_files()
        pass