## Questions to ask

- If CharField(null=False) has choices, how we should "clear" that field?
- If CharField(null=True) has choices, how we should "clear" that field? Should we add '' to choices?
- If CharField(null=True) is cleared, how we should "clear" that field?


```python
type_choices = ["normal", "additional", "extra_additional"]
model_type = models.CharField(null=False, choices=type_choices)

name = models.CharField() -> we will discuss that field
```

# OK BASICALLY...

## null=True blank=True

```python
name = models.CharField(null=True, blank=True)
```

You can create model via `MyModel.objects.create()` without specifying the field.
It create instance with `'model_type': None`.

You can create it via DRF without specyfying the field.
It create instance with `'model_type': None`.

You can create it via DRF with specified `field=null`.
It create instance with `'model_type': None`.

You can update it via DRF with specified `field=null`.
It create instance with `'model_type': None`.


## null=True blank=False

```python
name = models.CharField(null=True, blank=False)
```

You can create model via `MyModel.objects.create()` without specifying the field.
It create instance with `'model_type': None`.

You can create it via DRF without specyfying the field.
It create instance with `'model_type': None`.

You can create it via DRF with specified `field=null`.
It create instance with `'model_type': None`.

You can update it via DRF with specified `field=null`.
It create instance with `'model_type': None`.


## null=False blank=False

```python
name = models.CharField(null=False, blank=False)
```

You can create model via `MyModel.objects.create()` without specifying the field.
It create instance with `'model_type': ''` (with empty string).

You can't create it via DRF without specyfying the field.
You get `name -> this field is required`
If you add `required=False` to your serializer field, you can create the instance with `""` (empty string).

You can't create it via DRF with specified `field=null`.
Yout get `name ->this field may not be null`.
If you add `allow_null=True` to your serializer field, you'll get database INTEGRITY ERROR about NOT NULL CONSTRAINT.

You can't update it via DRF with specified `field=null`.
Yout get `name ->this field may not be null`.


## null=False blank=True

```python
name = models.CharField(null=False, blank=True)
```

You can create model via `MyModel.objects.create()` without specifying the field.
It create instance with `'name': ''` (with empty string).

You can create it via DRF without specyfying the field.
It create instance with `'name': ''` (with empty string).

You can't create it via DRF with specified `field=null`.
Yout get `name ->this field may not be null`.

You can't update it via DRF with specified `field=null`.
Yout get `name ->this field may not be null`.
