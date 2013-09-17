===============================
Validación de cuentas bancarias
===============================

Permite la validación de cuentas bancarias de terceros o empresas. Al añadir el
número de cuenta bancaria, debe añadir de qué país es la cuenta. Si la cuenta
no es correcta, un mensaje le notificará que revise el número de cuenta bancaria.

Este módulo se basa en una librería de validación de cuentas bancarias (banknumber)
que deberá ser instalada en su servidor de Tryton.
 
Dependiendo de si existe o no el método de validación de un país en concreto,
Tryton validará o no las cuentas bancarias para el mismo.
