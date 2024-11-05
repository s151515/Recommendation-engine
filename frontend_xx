'use client'

import { useState } from 'react'
import { Button } from "@/components/ui/button"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from "@/components/ui/card"

export default function RecommendationSystem() {
  const [category, setCategory] = useState('')
  const [mood, setMood] = useState('')
  const [suggestion, setSuggestion] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const categoryOptions = [
    { value: 'movies', label: 'Movies' },
    { value: 'food', label: 'Food' },
    { value: 'activities', label: 'Activities' },
    { value: 'tv_shows', label: 'TV Shows' },
  ]

  const moodOptions = {
    movies: ['comedy', 'drama', 'action', 'adventure', 'thriller'],
    food: ['spicy', 'sweet', 'healthy', 'savory', 'bitter'],
    activities: ['outdoor', 'indoor', 'learning', 'wellness'],
    tv_shows: ['comedy', 'drama', 'action', 'mystery', 'scifi'],
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    try {
      const response = await fetch('/api/get-suggestion', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ category, mood }),
      })
      const data = await response.json()
      setSuggestion(data.suggestion)
    } catch (error) {
      console.error('Error:', error)
      setSuggestion('An error occurred')
    }
    setIsLoading(false)
  }

  const handleNewSuggestion = async () => {
    await handleSubmit({ preventDefault: () => {} } as React.FormEvent)
  }

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle>Get a Suggestion</CardTitle>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="category" className="block text-sm font-medium text-gray-700">
              Category
            </label>
            <Select onValueChange={(value) => setCategory(value)}>
              <SelectTrigger>
                <SelectValue placeholder="Select a category" />
              </SelectTrigger>
              <SelectContent>
                {categoryOptions.map((option) => (
                  <SelectItem key={option.value} value={option.value}>
                    {option.label}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>
          {category && (
            <div>
              <label htmlFor="mood" className="block text-sm font-medium text-gray-700">
                Mood/Preference
              </label>
              <Select onValueChange={(value) => setMood(value)}>
                <SelectTrigger>
                  <SelectValue placeholder="Select your mood" />
                </SelectTrigger>
                <SelectContent>
                  {moodOptions[category as keyof typeof moodOptions].map((option) => (
                    <SelectItem key={option} value={option}>
                      {option.charAt(0).toUpperCase() + option.slice(1)}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
          )}
          <Button type="submit" disabled={isLoading || !category || !mood}>
            {isLoading ? 'Getting Suggestion...' : 'Get Suggestion'}
          </Button>
        </form>
      </CardContent>
      {suggestion && (
        <CardFooter className="flex flex-col items-start">
          <h3 className="text-lg font-medium">Suggestion:</h3>
          <p className="mt-2 text-gray-600">{suggestion}</p>
          <Button onClick={handleNewSuggestion} className="mt-4">
            Get Another Suggestion
          </Button>
        </CardFooter>
      )}
    </Card>
  )
}
