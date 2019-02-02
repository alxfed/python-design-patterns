"""
template_method.py
this is a test of the git plug-in fugitive.vim too
"""


import abc


class TemplateAbstractBaseClass(metaclass=abc.ABCMeta):
    def template_method(self):
        self._step_1()
        self._step_2()
        self._step_n()

    @abc.abstractmethod
    def _step_1(self):
        pass

    @abc.abstractmethod
    def _step_2(self):
        pass

    @abc.abstractmethod
    def _step_3(self):
        pass


class ConcreteImplementationClass(TemplateAbstractBaseClass):
    def _step_1(self): pass

    def _step_2(self): pass

    def _step_3(self): pass
