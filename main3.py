def find_potential_customers_v1():
    """找到去过普吉岛但是没去过新西兰的人
    """
    for phuket_record in users_visited_phuket:
        is_potential = True
        for nz_record in users_visited_nz:
            if phuket_record['first_name'] == nz_record['first_name'] and \
                    phuket_record['last_name'] == nz_record['last_name'] and \
                    phuket_record['phone_number'] == nz_record['phone_number']:
                is_potential = False
                break

        if is_potential:
            yield phuket_record
