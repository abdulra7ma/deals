from django.db.models import Count, Sum

from deals.apps.processor.models import Client, Item


def get_top_clients():
    top_clients = (
        Client.objects.annotate(
            total_money=Sum("transactions__total"),
        )
        .filter(
            transactions__item__in=Item.objects.filter(
                transaction__client__in=Client.objects.annotate(
                    total_money=Sum("transactions__total")
                ).order_by("-total_money")[:5]
            )
            .annotate(buyers=Count("transaction__client"))
            .filter(buyers__gte=2)
        )
        .order_by("-total_money")[:5]
    )

    for client in top_clients:
        client.gems = (
            Item.objects.filter(
                transaction__client=client,
                transaction__client__in=Client.objects.annotate(
                    total_money=Sum("transactions__total")
                ).order_by("-total_money")[:5],
            )
            .annotate(buyers=Count("transaction__client"))
            .filter(buyers__gte=2)
            .values_list("name", flat=True)
        )

    return top_clients
