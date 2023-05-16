def find_potential_customers_v2():
    nyc_record_idx = {
        (rec['first_name'], rec['last_name'], rec['phone_number'])
        for rec in tourists_visited_nyc
    }

    for rec in tourists_visited_hk:
        key = (rec['first_name'], rec['last_name'], rec['phone_number'])
        if key not in nyc_record_idx:
            yield rec
