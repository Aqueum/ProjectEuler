# inspired by RaviBansal7717 at https://projecteuler.net/thread=1;page=9#last 
print(
  sum(
    set(
      list(
        range(3,1000,3)
      ) 
      +
      list(
        range(5,1000,5)
      )
    )
  )
)