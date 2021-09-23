class Node(object):

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        to_print = [str(self.value)]
        current = self.next
        while current:
            to_print.append(str(current.value))
            current = current.next
        return "-".join(to_print)


def insert_node(head, val):
    previous_node = head
    current_node = head.next
    while current_node and current_node.value <= val:
        previous_node = current_node
        current_node = current_node.next
    new_node = Node(val)
    new_node.next = current_node
    previous_node.next = new_node
    return head


def merge_node(head_0, head_1):
    dummy_head = Node(0)
    current_node = dummy_head
    while head_0 and head_1:
        if head_0.value < head_1.value:
            current_node.next = head_0
            head_0 = head_0.next
        else:
            current_node.next = head_1
            head_1 = head_1.next
        current_node = current_node.next
    if head_0:
        current_node.next = head_0
    if head_1:
        current_node.next = head_1
    return dummy_head.next


def bucket_sort(a_list):
    n = len(a_list)
    if n < 2:
        return a_list
    max_value = float("-inf")
    for i in range(n):
        max_value = max(max_value, a_list[i])
    min_value = float("inf")
    for i in range(n):
        min_value = min(min_value, a_list[i])
    gap_length = max(1, (max_value - min_value) // (n - 1))
    bucket_size = (max_value - min_value) // gap_length + 1
    buckets = [Node(0) for i in range(bucket_size)]
    for i in range(n):
        bucket_index = (a_list[i] - min_value) // gap_length
        current_bucket = buckets[bucket_index]
        buckets[bucket_index] = insert_node(current_bucket, a_list[i])
    current_head = buckets[0].next
    for i in range(1, bucket_size):
        if buckets[i].next:
            current_head = merge_node(current_head, buckets[i].next)
    print("result link list:", current_head)
    result = []
    while current_head:
        result.append(current_head.value)
        current_head = current_head.next
    return result


if __name__ == "__main__":
    a_list = [3, 2, 5, 1, 8, 4]
    print(bucket_sort(a_list))