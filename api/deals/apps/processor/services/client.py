import csv
from io import TextIOWrapper

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, transaction
from django.http import HttpRequest
from django.utils.translation import gettext_lazy
from rest_framework import status
from rest_framework.response import Response

from deals.apps.processor.models import Transaction, Item, Client


class ClientService:
    """
    Service class that provides methods to interact with the `Client` model
    """

    @staticmethod
    def load_csv(request: HttpRequest):
        """
        Loads data from a CSV file into the database for the `Client` model
        :param request: path to the CSV file
        """

        with transaction.atomic():
            # Open the CSV file
            with TextIOWrapper(request.FILES["file"], encoding="utf-8") as f:
                # Create a CSV reader object
                reader = csv.DictReader(f)

                # Iterate over the rows in the CSV file
                for row in reader:
                    try:
                        # Get or create the client object
                        client, created = Client.objects.get_or_create(
                            username=row["customer"]
                        )

                        # Update the client's spent money
                        client.spent_money += float(row["total"])
                        client.gems.append(row['item'])
                        client.save()

                        # Get or create the item object
                        item, created = Item.objects.get_or_create(
                            name=row["item"],
                            defaults={
                                "total": row["total"],
                                "quantity": row["quantity"],
                            },
                        )

                        # Create a new transaction
                        item_transaction = Transaction.objects.create(
                            client=client,
                            item=item,
                            total=row["total"],
                            quantity=row["quantity"],
                            date=row["date"],
                        )

                        # Add the transaction to the client's transactions field
                        client.transactions.add(item_transaction)
                    except IntegrityError as e:
                        pass

                    except ObjectDoesNotExist as e:
                        pass

        return Response(
            data=gettext_lazy("Successfully processed the file"),
            status=status.HTTP_200_OK,
        )
