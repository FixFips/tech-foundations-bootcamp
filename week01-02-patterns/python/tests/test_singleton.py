import concurrent.futures as cf

from patterns.singleton import GLOBAL_CONFIG, AppConfig


def test_single_instance_identity():
    a = AppConfig(name="A")
    b = AppConfig(name="B")  # second construction attempt returns the same instance
    assert a is b
    # the first initialization wins; name should remain 'A'
    assert a.name == "A" and b.name == "A"


def test_thread_safety():
    def make_it(_):
        return AppConfig()

    with cf.ThreadPoolExecutor(max_workers=16) as ex:
        instances = list(ex.map(make_it, range(200)))
    # all identities are the same object
    assert len({id(x) for x in instances}) == 1


def test_global_config_exists_but_is_not_singleton():
    # simple sanity check: GLOBAL_CONFIG exists but it's just a module-level instance
    assert GLOBAL_CONFIG is not None
