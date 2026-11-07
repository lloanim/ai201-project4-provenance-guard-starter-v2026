Run 1:
== Part 1: 5 appeals on real content_ids ==
[PASS] c_79456503e95c  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_fcb96145d5ef  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_b21e471b5894  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_ab92249b5dda  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_ae4084b3c48c  appeal=200  log statuses=['decided', 'under_review']
5/5 passed

== Part 2: 3 appeals on a fake content_id ==
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist0'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist1'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist2'."}
3/3 passed

Run 2:
== Part 1: 5 appeals on real content_ids ==
[PASS] c_4bac96693c39  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_1f4ade06c3fd  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_b2c90537c32d  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_b9bce397547e  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_5d961c290e9c  appeal=200  log statuses=['decided', 'under_review']
5/5 passed

== Part 2: 3 appeals on a fake content_id ==
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist0'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist1'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist2'."}
3/3 passed

Run 3:
== Part 1: 5 appeals on real content_ids ==
[PASS] c_a96264da6c7d  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_efb6642a0329  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_4d7be6a86da7  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_b11f72657ee1  appeal=200  log statuses=['decided', 'under_review']
[PASS] c_d58e5c36b3ac  appeal=200  log statuses=['decided', 'under_review']
5/5 passed

== Part 2: 3 appeals on a fake content_id ==
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist0'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist1'."}
[PASS] status=404  body={'error': 'not_found', 'message': "No submission found with content_id 'c_doesnotexist2'."}
3/3 passed