from controllers.scrapper import ScrapperFactory, ScrapperJudiciales


def test_scrapper_judiciales_actor():
    """
    Test para verificar que el scrapper de actor se ejecute correctamente
    """

    scrapper = ScrapperFactory.create_scrapper("actor", "0968599020001")
    assert scrapper.process_execute == "Actor"


def test_scrapper_judiciales_demandado():
    """
    Test para verificar que el scrapper de demandado se ejecute correctamente
    """

    scrapper = ScrapperFactory.create_scrapper("demandado", "1791251237001")
    assert scrapper.process_execute == "Demandado"


def test_scrapper_judiciales():
    """
    Test para el scrapper de judiciales
    """

    scrapper_user = ScrapperFactory.create_scrapper("actor", "0968599020001")
    assert scrapper_user.process_execute == "Actor"
    scrapper = ScrapperJudiciales.get_causas(scrapper_user)
    assert scrapper is not None
    assert scrapper["causas"] is not None
    assert scrapper["process"] == "Actor"


def test_scrapper_judiciales_not_found():
    """
    Test para el scrapper de judiciales sin resultados
    """

    scrapper_user = ScrapperFactory.create_scrapper("actor", "231231231123")
    assert scrapper_user.process_execute == "Actor"
    scrapper = ScrapperJudiciales.get_causas(scrapper_user)
    assert scrapper is not None
    assert len(scrapper["causas"]) == 0
    assert scrapper["process"] == "Actor"
