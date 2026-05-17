import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Item


def login_page(request):
    return render(request, 'index.html')


def dashboard_page(request):
    return render(request, 'dashboard.html')


def itens_page(request):
    return render(request, 'itens.html')


def usuarios_page(request):
    return render(request, 'usuarios.html')


@csrf_exempt
@require_http_methods(["GET", "POST"])
def itens_api(request):
    if request.method == 'GET':
        itens = list(
            Item.objects.values(
                'id', 'nome', 'p_12', 'descricao_item', 'medidas', 'acabamento'
            )
        )
        return JsonResponse(itens, safe=False)

    data = json.loads(request.body.decode('utf-8'))
    item = Item.objects.create(
        nome=data['nome'],
        p_12=data.get('p_12'),
        descricao_item=data['descricao_item'],
        medidas=data['medidas'],
        acabamento=data['acabamento'],
    )
    return JsonResponse({'status': 'sucesso', 'item_id': item.id}, status=201)
