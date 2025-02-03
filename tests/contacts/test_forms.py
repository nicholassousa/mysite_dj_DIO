from contacts.forms import NameForm


def test_name_form_success():

    #given
    data = {"your_name": "John"}
    form = NameForm(data=data)

    #when
    result = form.is_valid()

    #then
    assert result is True

def test_name_from_your_name_max_length():

#given
    data = {"your_name": "John"*50}
    form = NameForm(data=data)

    #when
    result = form.is_valid()

    #then
    assert result is False


def test_name_form_fail():

    #given
    data = {}
    form = NameForm(data=data)

    #when
    result = form.is_valid()

    #then
    assert result is False

