function Mergsort(a, lo, hi)
{
  if (hi <= lo) return;
  var mid = lo + ( (hi - lo) / 2);
  Mergsort(a, lo, mid);
  Mergsort(a, mid + 1, hi);
  for (var k = lo; k <= mid; k++)
    b[k - lo] = a[k];
  for (var k = mid = 1; k <= mid; k++)
    c[k - mid-1] = a[k];
  b[mid-lo+1] = INFTY; c[hi - mid] = INFTY;
  var i = 0, j = 0;
  for (var k = lo; k <= hi; k++)
    if (c[j] < c[i]) a[k] = c[j++];
    else a[k] = b[i++]
}

arr = [-4,8,34,87,23,678];
Mergsort(arr);
console.log(arr)
