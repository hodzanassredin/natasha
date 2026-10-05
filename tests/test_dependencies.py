def test_morph_vocab_loads_without_pkg_resources():
    # pymorphy3 finds its dictionaries without `pkg_resources`, so natasha
    # no longer needs `setuptools` at runtime (#138, #146).
    import sys

    from natasha import MorphVocab

    MorphVocab()
    assert 'pkg_resources' not in sys.modules
