from django.shortcuts import render, redirect
from .forms import CuestionarioFormPag1, CuestionarioFormPag2
from .models import Universidad, Conflicto, Subconflicto, Orientacion

SUBCATEGORIAS = {
    "academico": [
        ("notas", "Notas"),
        ("evaluaciones", "Evaluaciones"),
        ("inscripciones", "Inscripción de asignaturas"),
    ],

    "administrativo": [
        ("matricula", "Matrícula"),
        ("certificados", "Certificados"),
        ("tramites", "Trámites"),
    ],

    "economico": [
        ("becas", "Becas"),
        ("aranceles", "Aranceles"),
        ("beneficios", "Beneficios estudiantiles"),
    ],

    "acoso": [
        ("docente", "Acoso por docente"),
        ("estudiante", "Acoso por estudiante"),
    ],

    "discriminacion": [
        ("genero", "Discriminación por género"),
        ("otro", "Otro tipo de discriminación"),
    ]
}


def cuestionariopaso1(request):
    """Paso 1"""

    if request.method == "POST":
        form = CuestionarioFormPag1(request.POST)

        if form.is_valid():

            request.session["universidad"] = form.cleaned_data["universidad"]
            request.session["conflicto"] = form.cleaned_data["conflicto"]

            return redirect("paso2")

    else:
        form = CuestionarioFormPag1()

    return render(
        request,
        "cuestionario/cuestionario.html",
        {
            "form": form,
            "paso": 1,
        }
    )

def cuestionariopaso2(request):

    conflicto = request.session.get("conflicto")

    if not conflicto:
        return redirect("cuestionario")

    form = CuestionarioFormPag2(request.POST or None)

    form.fields["subconflicto"].choices = SUBCATEGORIAS[conflicto]

    if request.method == "POST" and form.is_valid():

        subconflicto = form.cleaned_data["subconflicto"]
        derechos = form.cleaned_data["derechos"]

        universidad = request.session.get("universidad")

        orientacion = Orientacion.objects.filter(
            universidad__codigo=universidad,
            conflicto__codigo=conflicto,
            subconflicto__codigo=subconflicto,
        ).first()

        if orientacion:
            request.session["orientacion_id"] = orientacion.id

        request.session["derechos"] = derechos
        request.session["subconflicto"] = subconflicto

        universidad_obj = Universidad.objects.filter(
            codigo=universidad
        ).first()

        conflicto_obj = Conflicto.objects.filter(
            codigo=conflicto
        ).first()

        subconflicto_obj = Subconflicto.objects.filter(
            codigo=subconflicto
        ).first()

        return render(
            request,
            "cuestionario/resultado.html",
            {
                "orientacion": orientacion,
                "derechos": derechos,

                "universidad": universidad_obj.name if universidad_obj else universidad,
                "conflicto": conflicto_obj.name if conflicto_obj else conflicto,
                "subconflicto": subconflicto_obj.name if subconflicto_obj else subconflicto,
            }
        )

    return render(
        request,
        "cuestionario/cuestionario.html",
        {
            "form": form,
            "paso": 2,
        }
    )


def descarga(request):

    orientacion_id = request.session.get("orientacion_id")

    universidad_codigo = request.session.get("universidad")
    conflicto_codigo = request.session.get("conflicto")
    subconflicto_codigo = request.session.get("subconflicto")
    derechos = request.session.get("derechos")

    orientacion = Orientacion.objects.get(
        id=orientacion_id
    )

    universidad = Universidad.objects.get(
        codigo=universidad_codigo
    )

    conflicto = Conflicto.objects.get(
        codigo=conflicto_codigo
    )

    subconflicto = Subconflicto.objects.get(
        codigo=subconflicto_codigo
    )

    return render(
        request,
        "cuestionario/descarga.html",
        {
            "orientacion": orientacion,
            "derechos": derechos,
            "universidad": universidad.name,
            "conflicto": conflicto.name,
            "subconflicto": subconflicto.name,
        }
    )