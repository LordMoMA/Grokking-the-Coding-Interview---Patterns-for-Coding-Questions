def find_potential_customers_v1():
    for hk_record in users_visited_hk:
        is_potential = True
        for nyc_record in users_visited_nyc:
            if hk_record['first_name'] == nyc_record['first_name'] and \
                    hk_record['last_name'] == nyc_record['last_name'] and \
                    hk_record['phone_number'] == nyc_record['phone_number']:
                is_potential = False
                break

        if is_potential:
            yield hk_record
