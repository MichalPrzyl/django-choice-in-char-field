## Questions to ask

- If CharField(null=False) has choices, how we should "clear" that field?


```python
type_choices = ["normal", "additional", "extra_additional"]

model_type = models.CharField(null=False, choices=type_choices)
```

