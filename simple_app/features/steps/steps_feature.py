@given(u'blablabla')
def step_impl(context):
 assert True


@given(u'some bla')
def step_impl(context):
 assert True


@given(u'user is smart')
def step_impl(context):
 assert True


@given(u'is not stupid')
def step_impl(context):
 assert True


@when(u'he uses system')
def step_impl(context):
 assert True


@then(u'system is useful')
def step_impl(context):
 assert False
