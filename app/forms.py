from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class CardForm(FlaskForm):
    number = StringField('Номер карты', validators=[DataRequired()])


class PinForm(FlaskForm):
    pin = PasswordField('Пин-код', validators=[DataRequired()])


class OptionsForm(FlaskForm):
    balance = SubmitField('Баланс')
    cash = SubmitField('Снятие денег')
    ext = SubmitField('Выход')


class BalanceForm(FlaskForm):
    back = SubmitField('Назад')
    ext = SubmitField('Выход')


class CashForm(FlaskForm):
    amount = StringField('Сумма')
    back = SubmitField('Назад')
    ext = SubmitField('Выход')


class BillForm(FlaskForm):
    back = SubmitField('Назад')
    ext = SubmitField('Выход')


class BackForm(FlaskForm):
    back = SubmitField('Назад')
