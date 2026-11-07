Run 1:
== Part 1: 5 appeals on real content_ids ==
[PASS] c_e38676bce07d  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_38c23a74e153  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_cfff1bd46ffd  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_adb6a6aab544  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_384f713424bf  appeal=200  log statuses=['decided', 'under_review']
5/5 passed

== Part 2: 3 appeals on a fake content_id ==
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist0'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist1'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist2'."}
3/3 passed

Run 2:
== Part 1: 5 appeals on real content_ids ==
[PASS] c_22f0bc9372e4  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_2a10f3de7b17  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_265e65c8c7b4  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_6514cc3b25d3  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_e4c41f9c3077  appeal=200  log statuses=['decided', 'under_review']
5/5 passed

== Part 2: 3 appeals on a fake content_id ==
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist0'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist1'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist2'."}
3/3 passed

Run 3:
== Part 1: 5 appeals on real content_ids ==
[PASS] c_bc05e62d58cc  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_757ac27b34de  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_d8d0466a8808  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_fb5af3328fb8  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_c6776ed8d5d4  appeal=200  log statuses=['decided', 'under_review']
5/5 passed

== Part 2: 3 appeals on a fake content_id ==
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist0'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist1'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist2'."}
3/3 passed