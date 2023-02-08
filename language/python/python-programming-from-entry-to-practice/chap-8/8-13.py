def build_profile(first, last, **user_info):
    profile = {}
    profile['fitst_name'] = first
    profile['last_name'] = last

    for key, val in user_info.items():
        profile[key] = val

    # print(profile)
    return profile


user_profile = build_profile(
    'yu', 'haha', location='china', field='physics', language='chinese'
)

print(user_profile)
