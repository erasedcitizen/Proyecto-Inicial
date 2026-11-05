from django import forms

class CuestionarioFormPag1(forms.Form):

    universidad = forms.ChoiceField(
        label="¿De que universidad eres?",
        help_text="Selecciona la institución a la que perteneces. (Solo en la Región de Valparaíso)",
        choices=[
            ("utfsm", "Universidad Técnica Federico Santa María"),
            ("pucv", "Pontificia Universidad Católica de Valparaíso"),
        ],
        widget=forms.RadioSelect
    )

    conflicto = forms.ChoiceField(
        label="Elige la categoría de tu problema",
        help_text="Selecciona la opción que mejor describa la situación que estás experimentando.",
        choices=[
            ("academico", "Problemas Académicos (asignaturas, inscripciones, evaluaciones, notas)"),
            ("administrativo", "Problemas Administrativos (matrícula, certificados, trámites)"),
            ("discriminacion", "Discriminación (trato desigual o exclusión)"),
            ("acoso", "Acoso Académico (hostigamiento por docentes o estudiantes)"),
            ("economico", "Problemas Económicos (becas, aranceles o falta de recursos)"),
        ],
        widget=forms.RadioSelect
    )


class CuestionarioFormPag2(forms.Form):

    subconflicto = forms.ChoiceField(
        label="Elige tu problema",
        help_text="Selecciona la opción que mejor describa la situación que estás experimentando.",
        choices=[],
        widget=forms.RadioSelect
    )

    derechos = forms.ChoiceField(
        label="¿Conoces tus derechos como estudiante?",
        help_text="Indica si conoces los derechos educacionales de los estudiantes",
        choices=[
            ("si", "Sí, los conozco"),
            ("no", "No, no se cuales son."),
        ],
        widget=forms.RadioSelect
    )
    