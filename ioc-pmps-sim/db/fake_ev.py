from caproto.server import PVGroup, pvproperty


class FakeEVGroup(PVGroup):
    """
    PV group for fake photon energy readback
    """
    fake_eV = pvproperty(value=9500,
                         name='EV',
                         record='ao',
                         upper_alarm_limit=25000,
                         lower_alarm_limit=1000,
                         doc='Fake photon energy PV for '
                         + 'attenuator testing')

    def __init__(self, prefix, *, ioc, **kwargs):
        super().__init__(prefix, **kwargs)
        self.ioc = ioc

    @fake_eV.putter
    async def fake_eV(self, instance, value):
        if value < 0:
            raise ValueError('Invalid photon energy')
